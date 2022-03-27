"""Function to retreive the previous quarter, based on the provided date."""
def get_prev_quarter(yyyy, mm, dd):
    if((mm==1) or (mm==2) or (mm==3)):
        quarter_date = f"""{yyyy-1}-12-31"""
    elif((mm==4) or (mm==5) or (mm==6)):
        quarter_date = f"""{yyyy}-03-31"""
    elif((mm==7) or (mm==8) or (mm==9)):
        quarter_date = f"""{yyyy}-06-30"""
    elif((mm==10) or (mm==11) or (mm==12)):
        quarter_date = f"""{yyyy}-09-30"""
    return (quarter_date)
    
print(get_prev_quarter(2025,1,27))