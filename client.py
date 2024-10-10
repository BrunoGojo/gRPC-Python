import grpc
import user_pb2
import user_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        name = input("Coloque seu nome: ")
        phone = input("Coloque seu número: ")
        email = input("Coloque seu E-Mail: ")

        request = user_pb2.UserRequest(name=name, phone=phone, email=email)
        response = stub.CreateUser(request)
        
        print(response.message)

if __name__ == '__main__':
    run()
