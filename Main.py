# sudo docker -H tcp://127.0.0.1:2375 ps
# https://medium.com/@sudarakayasindu/enabling-and-accessing-docker-engine-api-on-a-remote-docker-host-on-ubuntu-16-04-2c15f55f5d39
import docker


class XnfvDocker:
    def __init__(self, serverAddress, serverPort):
        self.serverAddress = serverAddress
        self.serverPort = serverPort
        self.dockerClient = None
        self.CreateDockerClient()

    def CreateDockerClient(self):
        self.dockerClient = docker.DockerClient(base_url="tcp://" + self.serverAddress + ":" + self.serverPort)

    # Docker Image-Related functions ---------------------------------------
    def ImgDetailedList(self):
        temp = []
        for image in self.dockerClient.images.list():
            temp.append(image.attrs)
        return temp

    def ImgNameList(self):
        temp = []
        for image in self.dockerClient.images.list():
            temp.append(image.attrs['RepoTags'][0])
        return temp

    # Docker Container-Related functions ---------------------------------------
    def ContainerDetailedList(self):
        return self.dockerClient.containers.list()

xnfv = XnfvDocker("192.168.1.5", "2375")
for ii in xnfv.ContainerDetailedList():
    print(ii)
