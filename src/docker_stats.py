import docker
import datetime
import arrow

def docker_stats():
    final_list = []
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    data = client.containers.list(filters = {
        "status": "running"
    })
    for item in data:
        final_list.append([item.name.upper(), arrow.get(item.attrs['State']['StartedAt']).humanize()])
    return final_list

if __name__ == "__main__":
    pass