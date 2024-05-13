import csv

# file path
csvpath = "Resources/budget_data.csv"

#the variable for counting out the months
counting_months = 0

#the variable for the net profit
net_profit = 0 

# create list and add variable for changes 
prior_month_profit = 0
changes = []
monthly_changes = []

# open the csv using the utf-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # read the header row first 
        csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")

        # Read each row of data after the header
        for row in csvreader:
            print(row)

            #counting out the months
            counting_months = counting_months + 1

            #adding the profit
            net_profit = net_profit + int(row[1])

            #subtract this months profit from prior month then, append any change to the list

            if (counting_months == 1):
        
                prior_month_profit = int(row[1])

            else:
                change = int(row[1]) - prior_month_profit
                changes.append(change)
                monthly_changes.append(row[0])

                prior_month_profit = int(row[1])
    
        print(counting_months)
        print(net_profit)
        print(len(changes))
        ave_change = sum(changes) / len(changes)
        print(ave_change)
        max_change = max(changes)
        max_month_indx = changes.index(max_change)
        max_month = monthly_changes[max_month_indx]
        print(max_change)
        print(max_month)

        min_change = min(changes)
        min_month_indx = changes.index(min_change)
        min_month = monthly_changes[min_month_indx]
        print(min_change)
        print(min_month)


#create text table (code received from xpert)
financial_data = {
    "Total Months": 86,
    "Total": "$22564198",
    "Average Change": "$-8311.11",
    "Greatest Increase in Profits": "Aug-16 ($1862002)",
    "Greatest Decrease in Profits": "Feb-14 ($-1825558)"
}

# Generate the financial data text
financial_data_text = ""
for key, value in financial_data.items():
    financial_data_text += f"{key}: {value}\n"

print(financial_data_text)