# Extract numeric data from excel files
def extract_data_from_csv(csv_filename,column_name):
    import numpy as np
    import pandas as pd
    
    data = pd.read_csv(csv_filename)
    
    data_allValues = data[column_name].values
    
    data_realValues_ind = np.nonzero(~np.isnan(data_allValues)) # Find all real (~NaN) values in train_Age\n",
    data_realValues = data_allValues[data_realValues_ind]
    
    return(data_allValues,data_realValues)
# End of extract_data_from_csv"

############################################
# Extract string data from excel files
def extract_str_data_from_csv(csv_filename,column_name):
    import numpy as np
    import pandas as pd
    
    data = pd.read_csv(csv_filename)
    
    data_allValues = data[column_name].values
    
    return(data_allValues)
# End of extract_str_data_from_csv"