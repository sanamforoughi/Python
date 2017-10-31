import numpy as np
from pandas import Series, DataFrame 

# The discounted payback period is one of several capital budget methods use to evaluate capital investments. 
# It gives the number of years requied to recover the original investment in a project. 
# It takes into account the time value of money by discounting the future cash flows at a desired rate of return.

#Desired rate of return, is say 10%
rate= 0.1 #don't use a fraction

# Amounts in millions, Also here you're obviously making the assumption that the cash flows are the same.
cash_flows = [-750] + [175] * 7
rate, cash_flows

# print cash_flows # This is just to show off really

#Now you want to arrange them in a data frame, so Year and the Undiscounted rate

cf_df = DataFrame(cash_flows, columns=['UndiscountedCashFlows'])
cf_df.index.name = 'Year'

# print cf_df #You don't actually need this

# Now you want to calculate the PV using numpy's BUILT IN npv(method). Then uou add them up. 


cf_df['DiscountedCashFlows'] = np.pv(rate=rate, pmt=0, nper=cf_df.index, fv=-cf_df['UndiscountedCashFlows'])
#cf_df

# print cf_df

cf_df['CumulativeDiscountedCashFlows'] = np.cumsum(cf_df['DiscountedCashFlows'])
print cf_df

#Full year
final_full_year = cf_df[cf_df.CumulativeDiscountedCashFlows < 0].index.values.max()
print final_full_year

#Fractional
fractional_yr = -cf_df.CumulativeDiscountedCashFlows[final_full_year ] / cf_df.DiscountedCashFlows[final_full_year + 1]
print fractional_yr

#total PB period
payback_period = final_full_year + fractional_yr
print payback_period

# Saving the above code as a function and calling it on different projects

def discounted_payback_period(rate, cash_flows=list()):    
    cf_df = DataFrame(cash_flows, columns=['UndiscountedCashFlows'])
    cf_df.index.name = 'Year'
    cf_df['DiscountedCashFlows'] = np.pv(rate=rate, pmt=0, nper=cf_df.index, fv=-cf_df['UndiscountedCashFlows'])
    cf_df['CumulativeDiscountedCashFlows'] = np.cumsum(cf_df['DiscountedCashFlows'])
    final_full_year = cf_df[cf_df.CumulativeDiscountedCashFlows < 0].index.values.max()
    fractional_yr = -cf_df.CumulativeDiscountedCashFlows[final_full_year ] / cf_df.DiscountedCashFlows[final_full_year + 1]
    payback_period = final_full_year + fractional_yr
    return payback_period
