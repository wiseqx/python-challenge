import csv
import os

months=[]
total_amount=0
max_amount=0
min_amount=0
profit_change=[]

pybank_csv = os.path.join("../", "Unit3 - Python_Homework_PyBank_Resources_budget_data.csv")

with open(pybank_csv,'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    #skip header
    next(csv_reader,None)
    csv_list=list(csv_reader)

    #The total number of months included in the dataset
    total_month=len(csv_list)

    previous_profit_num=int(csv_list[0][1])
    for row in range(len(csv_list)):
        #The net total amount of "Profit/Losses" over the entire period
        total_amount+=int(csv_list[row][1])

        #Calculate every change in "Profit/Losses" over the entire period
        net_change=int(csv_list[row][1])-previous_profit_num
        profit_change.append(net_change)
        previous_profit_num=int(csv_list[row][1])
        
    #calculate the average of the changes in "Profit/Losses" over the entire period
    average_change=round(sum(profit_change)/(len(csv_list)-1),2)

    #The greatest increase in profits (date and amount) over the entire period
    for i in range(len(profit_change)):
        if int(profit_change[i])>max_amount:
            max_index_number=i
            max_amount=int(profit_change[i])
        elif int(profit_change[i])<min_amount:
            min_index_number=i
            min_amount=int(profit_change[i])
    
    #print summary table
    Summary_table="Financial Analysis \n" \
    +str("-"*30)+"\n" \
    +"Total Months: "+str(total_month) +"\n" \
    +"Total: $"+str(total_amount) +"\n" \
    +"Average  Change: $" +str(average_change) +"\n" \
    +"Greatest Increase in Profits: "+str(csv_list[max_index_number][0])+ " ($"+str(profit_change[max_index_number])+")\n" \
    +"Greatest Decrease in Profits: "+str(csv_list[min_index_number][0])+" ($"+str(profit_change[min_index_number])+")"
    print(Summary_table)

#write to a text file
output_file = open("PyBank_result.txt","w") 
output_file.write(Summary_table)
output_file.close()