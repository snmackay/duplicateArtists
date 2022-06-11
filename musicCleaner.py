import os

#do you have an old music library you want to merge with your main library?
#This will tell you if the artist already exists.
#I wrote this in like 5 minutes to do something

#Sean Mackay

def main():
    print("enter path to your main library")
    server_path=input("::")
    print("enter path to music you want to add")
    dupepath=input("::")

    server_list=os.listdir(server_path)
    print(len(server_list))
    dupe_list=os.listdir(dupepath)
    print(len(dupe_list))


    ret_list=[]
    for i in dupe_list:
        if i in server_list:
            ret_list.append(i)
        else:
            stripped=i.rstrip()
            stripped=stripped.strip('_')
            if stripped in server_list:
                ret_list.append(stripped)
    #have an empty file named duplicateArtists.txt
    file=open("duplicateArtists.txt", 'w')
    for k in ret_list:
        file.write(k)
        file.write('\n')

main()
