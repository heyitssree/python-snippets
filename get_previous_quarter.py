def get_prev_quarter(yyyy, mm, dd):
    if((mm=="01") or (mm=="02") or (mm=="03")):
        quarter_date = f"""{int(yyyy)-1}-12-31"""
    elif((mm=="04") or (mm=="05") or (mm=="06")):
        quarter_date = f"""{yyyy}-03-31"""
    elif((mm=="07") or (mm=="08") or (mm=="09")):
        quarter_date = f"""{yyyy}-06-30"""
    elif((mm=="10") or (mm=="11") or (mm=="12")):
        quarter_date = f"""{yyyy}-09-30"""
    return (quarter_date)
    
print(get_prev_quarter("2025","02","27"))