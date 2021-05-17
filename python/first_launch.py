
def first_launch():
    import grpc_generator
    grpc_generator.main()
    import main
    main.launch()


if __name__ == '__main__':
    first_launch()
