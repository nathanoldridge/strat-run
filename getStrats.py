def getDailyStrats(hist):
    current_day = hist.iloc[-1]
    current_day_high = current_day['High']
    current_day_low = current_day['Low']
    previous_day = hist.iloc[-2]
    previous_day_high = previous_day['High']
    previous_day_low = previous_day['Low']
    two_days_ago = hist.iloc[-3]
    two_days_ago_high = two_days_ago['High']
    two_days_ago_low = two_days_ago['Low']

    current_day_strat = None
    if current_day_high <= previous_day_high and current_day_low >= previous_day_low:
        current_day_strat = "1"
    elif current_day_high > previous_day_high and current_day_low < previous_day_low:
        current_day_strat = "3"
    elif current_day_high > previous_day_high:
        current_day_strat = "2u"
    else:
        current_day_strat = "2d"
    
    previous_day_strat = None
    if previous_day_high <= two_days_ago_high and previous_day_low >= two_days_ago_low:
        previous_day_strat = "1"
    elif previous_day_high > two_days_ago_high and previous_day_low < two_days_ago_low:
        previous_day_strat = "3"
    elif previous_day_high > two_days_ago_high:
        previous_day_strat = "2u"
    else:
        previous_day_strat = "2d"
    
    return previous_day_strat + "-" + current_day_strat



def getWeeklyStrats(hist):
    past_twenty_days = hist.iloc[-20:]
    past_twenty_days = past_twenty_days.reset_index()
    for x in range(-1,-5,-1): # Count backwards through DataFrame
        #print("**")
        #print("Checking x=",x)
        #print(past_twenty_days.iloc[x]['Date'])
        #print(past_twenty_days.iloc[x-1]['Date'])
        differenceInDays = str(past_twenty_days.iloc[x]['Date'] - past_twenty_days.iloc[x-1]['Date'])[0]
        #print(differenceInDays, "days difference")
        current_week = past_twenty_days[x:]
        if int(differenceInDays) != 1:
            break

    for y in range(x-1,x-6,-1):
        #print("**")
        #print("Checking y=",y)
        #print(past_twenty_days.iloc[y]['Date'])
        #print(past_twenty_days.iloc[y-1]['Date'])
        differenceInDays = str(past_twenty_days.iloc[y]['Date'] - past_twenty_days.iloc[y-1]['Date'])[0]
        #print(differenceInDays, "days difference")
        previous_week = past_twenty_days[y:x]
        if int(differenceInDays) != 1:
            break

    for z in range(y-1,y-6,-1):
        #print("**")
        #print("Checking y=",z)
        #print(past_twenty_days.iloc[z]['Date'])
        #print(past_twenty_days.iloc[z-1]['Date'])
        differenceInDays = str(past_twenty_days.iloc[z]['Date'] - past_twenty_days.iloc[z-1]['Date'])[0]
        #print(differenceInDays, "days difference")
        two_weeks_ago = past_twenty_days[z:y]
        if int(differenceInDays) != 1:
            break

    #print("CURRENT WEEK")
    #print(current_week)
    current_week_low = current_week.min()['Low']
    current_week_high = current_week.max()['High']
    #print("PREVIOUS WEEK")
    #print(previous_week)
    previous_week_low = previous_week.min()['Low']
    previous_week_high = previous_week.max()['High']
    #print("TWO WEEKS AGO")
    #print(two_weeks_ago)
    two_weeks_ago_low = two_weeks_ago.min()['Low']
    two_weeks_ago_high = two_weeks_ago.max()['High']

    current_week_strat = None
    if current_week_high <= previous_week_high and current_week_low >= previous_week_low:
        current_week_strat = "1"
    elif current_week_high > previous_week_high and current_week_low < previous_week_low:
        current_week_strat = "3"
    elif current_week_high > previous_week_high:
        current_week_strat = "2u"
    else:
        current_week_strat = "2d"
    
    previous_week_strat = None
    if previous_week_high <= two_weeks_ago_high and previous_week_low >= two_weeks_ago_low:
        previous_week_strat = "1"
    elif previous_week_high > two_weeks_ago_high and previous_week_low < two_weeks_ago_low:
        previous_week_strat = "3"
    elif previous_week_high > two_weeks_ago_high:
        previous_week_strat = "2u"
    else:
        previous_week_strat = "2d"
    
    return previous_week_strat + "-" + current_week_strat

#print(getDailyStrats(hist), "on the daily")
#print(getWeeklyStrats(hist), "on the weekly")




