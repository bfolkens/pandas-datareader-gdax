import pandas as pd
import numpy as np
import gdax
from datetime import datetime, timedelta
from time import sleep


def get_data_gdax(product, granularity=30*60, start=(datetime.now() - timedelta(days=1)), end=datetime.now(), delay=1):
    public_client = gdax.PublicClient()
    data_frames = []

    # GDAX allows 200 max per retrieve
    step = timedelta(seconds=(granularity * 200))

    periods = (end - start).total_seconds() / granularity
    period_start = start

    # Only break up the requests into chunks if it makes sense
    if (granularity * 200) > (end - start).total_seconds():
        period_end = end
    else:
        period_end = start + step

    while period_end <= end:
        # Retrieve the set
        records = public_client.get_product_historic_rates(product, granularity=granularity, start=period_start.isoformat(), end=period_end.isoformat())
        if not isinstance(records, (list)):
            raise TypeError("Instance is not a list: %s" % records)

        # GDAX has a strict use policy
        sleep(delay)

        # Iterate and observe any remaining elements after boundary
        period_start += step
        period_end += step
        if period_end > end and period_start < end:
            period_end = end

        if not records:
            continue

        # Convert to Pandas DataFrame
        records = np.array(records)
        df = pd.DataFrame(records[:,1:], index=records[:,0], columns=['Low', 'High', 'Open', 'Close', 'Volume'])
        df.index = pd.to_datetime(pd.to_numeric(df.index), utc=True, unit='s')
        df = df.sort_index(ascending=True)
        data_frames.append(df)

    return pd.concat(data_frames)
