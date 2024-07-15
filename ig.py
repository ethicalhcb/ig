import os

# Request the version to be installed
print("check here => https://go.dev/dl/")
version = input("Which version of Golang do you want to install? ")

# Downloading and installing Golang
os.system(f"sudo apt update")
os.system(f"wget https://golang.org/dl/go{version}.linux-amd64.tar.gz")
os.system(f"sudo tar -C /usr/local -xzf go{version}.linux-amd64.tar.gz")

# Configuration of the environment
os.system(f"echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc")
os.system(f"echo 'export GOPATH=$HOME/go' >> ~/.bashrc")
os.system(f"echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc")
os.system(f"source ~/.bashrc")

# ok
print("Golang install successful !" )