import csv
import os

row_count=0
candidates_list=[]
vote_dict={}

pypoll_csv = os.path.join("../", "Unit3 - Python_Homework_PyPoll_Resources_election_data.csv")

with open(pypoll_csv,'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader,None)
    for row in csv_reader:
        row_count+=1
        #Count the total number of votes each candidate won
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            vote_dict[str(row[2])]=[1]
        else:
            vote_dict[str(row[2])][0]+=1

    #Sort the winner of the election based on popular vote
    num_of_votes=0
    for key in vote_dict.keys():
        if int(vote_dict[key][0]) > num_of_votes:
            num_of_votes=int(vote_dict[key][0])
            winner_name=key

    #Count the percentage of votes each candidate won
    total_vote=sum([i[0] for i in vote_dict.values()])
    for name in candidates_list:
        if name in vote_dict:
            percentage_of_vote='{:.3%}'.format(float(vote_dict[str(name)][0]/total_vote))
            vote_dict[str(name)].append(percentage_of_vote)

    #print info and write to a new text file
    with open("PyPoll_result.txt","w") as output_file:
        #first two lines
        title='Election Results \n'+"-"*30+"\n"+"Total Votes: "+str(total_vote)+"\n"+"-"*30+"\n"
        print(title)
        output_file.write(title)
        for name in candidates_list:
            #candidate info
            candidate_info=name+": "+str(vote_dict[str(name)][1])+" ("+str(vote_dict[str(name)][0])+")"+"\n"
            print(candidate_info)
            output_file.write(candidate_info)
        #winner info
        Winner="-"*30+"\n"+"Winner: "+winner_name+"\n"+"-"*30
        print(Winner)
        output_file.write(Winner)
