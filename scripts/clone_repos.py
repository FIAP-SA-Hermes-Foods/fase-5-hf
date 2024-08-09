import subprocess

print("Type a input\n[1] - Clone\n[2] - Update\n[3] - Remove: ")

user_input = input()

api_services = [
    "service-hf-client-p5",
    "service-hf-orch-p5",
    "service-hf-order-p5",
    "service-hf-payment-p5",
    "service-hf-product-p5",
    "service-hf-voucher-p5",
]

orchs = [
    "orch-hf-p5",
]

pubs = [
    "pub-hf-client-p5",
    "pub-hf-orch-p5",
    "pub-hf-order-p5",
    "pub-hf-product-p5",
    "pub-hf-voucher-p5",
]

subs = [
    "sub-hf-client-p5",
    "sub-hf-orch-p5",
    "sub-hf-order-p5",
    "sub-hf-product-p5",
    "sub-hf-voucher-p5",
]

infra = [
    "hf-infra",
]

def clone_repos():
    git_clone_cmd = []

    for repo in api_services:
        strCmd = "git clone https://github.com/FIAP-SA-Hermes-Foods/"+repo+".git"
        git_clone_cmd.append(strCmd)

    for repo in orchs:
        strCmd = "git clone https://github.com/FIAP-SA-Hermes-Foods/"+repo+".git"
        git_clone_cmd.append(strCmd)

    for repo in pubs:
        strCmd = "git clone https://github.com/FIAP-SA-Hermes-Foods/"+repo+".git"
        git_clone_cmd.append(strCmd)

    for repo in subs:
        strCmd = "git clone https://github.com/FIAP-SA-Hermes-Foods/"+repo+".git"
        git_clone_cmd.append(strCmd)

    for repo in infra:
        strCmd = "git clone https://github.com/FIAP-SA-Hermes-Foods/"+repo+".git"
        git_clone_cmd.append(strCmd)


    commands = [
        "mkdir api-service",
        "mkdir orch",
        "mkdir pub",
        "mkdir sub",
        "mkdir infra",
    ]

    commands = commands + git_clone_cmd

    for cmd in commands:
        subprocess.call(cmd.split(), cwd='./')

    for repo in api_services:
        subprocess.call(["mv", repo, "api-service"], cwd='./')

    for repo in orchs:
        subprocess.call(["mv", repo, "orch"], cwd='./')

    for repo in pubs:
        subprocess.call(["mv", repo, "pub"], cwd='./')

    for repo in subs:
        subprocess.call(["mv", repo, "sub"], cwd='./')

    for repo in infra:
        subprocess.call(["mv", repo, "infra"], cwd="./")

    print("All repos has been cloned with success!")

def update_repos():
    for repo in api_services:
        print("Updating "+repo+"...\n")
        subprocess.call(['git', 'pull'], cwd='./api-service/'+repo) 

    for repo in orchs:
        print("Updating "+repo+"...\n")
        subprocess.call(['git', 'pull'], cwd='./orch/'+repo) 

    for repo in pubs:
        print("Updating "+repo+"...\n")
        subprocess.call(['git', 'pull'], cwd='./pub/'+repo) 

    for repo in subs:
        print("Updating "+repo+"...\n")
        subprocess.call(['git', 'pull'], cwd='./sub/'+repo)  

    for repo in infra:
        print("Updating "+repo+"...\n")
        subprocess.call(['git', 'pull'], cwd='./infra/'+repo)

    print("All repos has been updated with success!")


def remove_repos():
    commands = [
        "rm -rf api-service",
        "rm -rf orch",
        "rm -rf pub",
        "rm -rf sub",
        "rm -rf infra",
    ]

    for cmd in commands:
        subprocess.call(cmd.split(), cwd='./')

    print("All repos has been removed with success!")


if (user_input == "1"):
    clone_repos()
elif (user_input == "2"):
    update_repos()
elif (user_input == "3"):
    remove_repos()
else:
    print("Invalid input")


