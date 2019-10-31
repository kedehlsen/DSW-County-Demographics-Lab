import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(high_income_counties(counties))
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(lowest_median_income(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))

def high_income_counties(counties):
    """Return a LIST of the counties with a median household income over $90,000."""
    list = []
    for data in counties:
        if data['Income']['Median Household Income'] > 90000:
            list.append(data['County'])
    return list

def lowest_median_income(counties):
    """Return a name of a county with the lowest median household income"""
    min = counties[0]['Income']['Median Household Income']
    county = counties[0]['County']
    for data in counties:
        if data['Income']['Median Household Income'] < min:
            min = data['Income']['Median Household Income']
            county = data['County']
    return county

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    #Hint: you can use < to compare strings in Python. ex) "cat" < "dog" gives the value True
    county = counties[0]['County']
    for data in counties:
        if data['County'] < county:
            county = data['County']
    return county
    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    percent = counties[0]['Age']['Percent Under 18 Years']
    for data in counties:
        if data['Age']['Percent Under 18 Years'] > percent:
            percent = data['Age']['Percent Under 18 Years']
    return percent

def county_most_under_18(counties):
    """Return the name a county with the highest percent of under 18 year olds."""
    percent = counties[0]['Age']['Percent Under 18 Years']
    county = counties[0]['Age']['Percent Under 18 Years']
    for data in counties:
        if data['Age']['Percent Under 18 Years'] > percent:
            percent = data['Age']['Percent Under 18 Years']
            county = data['County']
    return county
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #1. Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    states={}
    for data in counties:
        if data['State'] not in states:
            states[data['State']] = 1
        else:
            states[data['State']] += 1
    #2. Find the state in the dictionary with the most counties
    countynum = 'CA'
    for state in states:
        if states[state] > states[countynum]:
            countynum = state
    #3. Return the state with the most counties
    return countynum
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    percent = counties[0]["Education"]["Bachelor's Degree or Higher"]
    county = counties[0]["Education"]["Bachelor's Degree or Higher"]
    for data in counties:
        if data["Education"]["Bachelor's Degree or Higher"] > percent:
            percent = data["Education"]["Bachelor's Degree or Higher"]
            county = data['County']
    return county
    
if __name__ == '__main__':
    main()
