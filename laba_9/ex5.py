def user_connection(username):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"

def establish_connection(auth=True):
    import random
    id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"
        
def connection():
    import random
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]
            
def write_to_file(f_obj):
    while True:
        m = yield
        f_obj.write(m+'\n')

def connect_user():
    while True:
        id = yield
        f = open('./messages/'+id+'.txt', 'w')
        w_c = write_to_file(f)
        next(w_c)
        yield w_c
    
def task_coroutine():
    authorized = {}
    user_corotine = connect_user()
    next(user_corotine)
    while True:
        a, b = (yield).split()
        if a == 'auth':
            authorized[b] = user_corotine.send(b)
            next(user_corotine)
        elif a == 'disconnect':
            authorized.pop(b, None)
        else:
            try:
                authorized[a].send(b)
            except KeyError:
                None
                

c = task_coroutine()
next(c)
for i in connection():
    c.send(i)
    
tl = TextLoader('./messages/')
for t in tl:
    print(t)