


#Changing the mining configuration
c = "stage_one_hashing_threads 96 stage_two_hashing_threads 96 io_threads 50 randomx_bulk_hashing_iterations 64"


#Large pages
l = "enable randomx_large_pages"


#add spesifict directory for Arweave data
p_path = "data_dir <path>"


#Start mining
m = "mine"


#Syncing the weave
s = "sync_jobs 80"


#Do not Sync
ns = "syn_jobs 0"


WalletAddress = "<your mining address here>"

#################### CHANGE HERE ####################
#Add the letters that represent your commands to the Arweave node

CMD = [m,s]

################## END CHANGE ZONE ##################




##### DO NOT CHANGE CODE BELOW /!\ #####

from subprocess import check_call

def GenerateSyntax(txt, Wallet):
    cmd="echo "+"./bin/start "+txt.strip()+" mining_addr "+Wallet.strip()+" peer 188.166.200.45 peer 188.166.192.169 peer 163.47.11.64 peer 139.59.51.59 peer 138.197.232.192"+"|clip"
    return check_call(cmd, shell=True)

cmdMaker = ""

for i in CMD :
    cmdMaker += i
    cmdMaker += " "
synText = cmdMaker[:-1]

GenerateSyntax(synText, WalletAddress)

