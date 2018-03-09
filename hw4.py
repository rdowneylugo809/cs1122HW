import socket

def get_list_from_data(str):
    lst = []
    i = 0
    n = len(str)
    for j in range(n):
        if(str[j]==' '):
            lst.append(int(str[i:j]))
            i = j
        elif(j+1 == n):
            lst.append(int(str[i+1:j+1]))
    return lst

def convert_list_to_string(lst):
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    return ' '.join(lst) + '\n'

def bub_sort(lst):
    n = len(lst) -1
    sort = True
    while(n>0 and sort):
        sort = False
        for i in range(n):
            if(lst[i]>lst[i+1]):
                sort = True
                lst[i],lst[i+1] = lst[i+1],lst[i]
        n -= 1
    return lst

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('chalbroker.cs1122.engineering.nyu.edu', 3120)
    sock.connect(server_address)

    try:
        print(sock.recv(1024))

        sock.send("rdl394\n".encode())
        print(sock.recv(1024))

        data = sock.recv(1024).decode("utf8")
        print(data)

        unsort = data[100:149].replace(', ',' ')
        lst = get_list_from_data(unsort)
        sort_list = bub_sort(lst)
        ans = convert_list_to_string(sort_list)
        print(ans)
        sock.send(ans.encode())
        data = sock.recv(1024).decode("utf8")
        print(data)
    finally:
        sock.close()

main()