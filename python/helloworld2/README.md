## Generate gRPC code

From the `helloworld2` directory run
`$ python -m grpc_tools.protoc -I../../protos --python_out=. --pyi_out=. --grpc_python_out=. ../../protos/helloworld2.proto`
