import subprocess
import getpass


NUM_NETWORKS = 3

class NetworkManager():
    def __init__(self):
        self.networks_list = []

    def display_networks(self):
        """
        Displays three wifi networks with strongest signal
        """
        output = subprocess.run("nmcli -g SSID,SIGNAL dev wifi",
                                shell=True, capture_output=True, text=True)
        # "nmcli -g SSID,SIGNAL dev wifi" -g means get-values (SSID and SIGNAL),
        # dev means devices, capture_output prevents the output on the
        # terminal and captutres it in output.stdout
        # text = True decodes the output to text format otherwise we will have
        # to use output.stdout.decode()

        self.networks_list = output.stdout.split("\n")
        self.networks_list.pop() # remove last element which is empty string

        self.filter_strong_networks()

        print("Your available wifi networks are:")
        for num, network in enumerate(self.networks_list):
            # print only the SSID (hence removing signal values)
            print(f"{num+1}. {network.split(':')[0]}") # 0 index has SSID

        return

    def filter_strong_networks(self):
        """
        Filter 3 strongest signal networks from all available networks
        """
        # sort based on signal values (which is at index 1)
        self.networks_list = sorted(
            self.networks_list, key=lambda x: int(x.split(":")[1]), reverse=True)
        self.networks_list = self.networks_list[:NUM_NETWORKS]
        return

    def choose_network(self):
        """
        Gets input for the desired network, validates the input, and
        then connects to the network if input_number and password for
        the desired network are correct.
        """
        while True:
            try:
                num = int(input("Your choice: "))
                if num > 0 and num <= len(self.networks_list):
                    break
                else:
                    print("Invalid input, please try again.")
            except ValueError as ve:
                print(ve)

        # get SSID of desired_network
        desired_network = self.networks_list[num-1].split(":")[0]
        password = getpass.getpass("Password: ")

        self.connect_to_network(desired_network, password)
        return

    def connect_to_network(self, desired_network, password):
        """
        Connects to the desired network using SSID and password
        """
        command = f'nmcli device wifi connect "{desired_network}" password "{password}"'
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    nm = NetworkManager()
    nm.display_networks()
    nm.choose_network()
