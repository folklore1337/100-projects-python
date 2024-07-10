from qbittorrent import Client

# Подключение к qBittorrent Web UI
qb = Client("http://127.0.0.1:8080/")

qb.login("admin", "123456")  

magnet_link = "magnet:?xt=urn:btih:abb33766b319a89e00e331727a946c33ad3ecdcc" 

qb.download_from_link(magnet_link)
