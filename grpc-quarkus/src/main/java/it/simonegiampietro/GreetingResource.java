package it.simonegiampietro;

import io.quarkus.grpc.runtime.annotations.GrpcService;
import it.simonegiampietro.another.AnotherHelloWorldServiceGrpc;
import it.simonegiampietro.another.AnotherRequest;
import it.simonegiampietro.another.AnotherResponse;
import it.simonegiampietro.hello.HelloWorldRequest;
import it.simonegiampietro.hello.HelloWorldServiceGrpc;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.inject.Inject;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.Arrays;
import java.util.List;

@Path("/")
public class GreetingResource {

    private static final Logger logger = LoggerFactory.getLogger(GreetingResource.class);

    @Inject
    @GrpcService("hello-service")
    HelloWorldServiceGrpc.HelloWorldServiceBlockingStub blocking;
    @Inject
    @GrpcService("hello-service")
    AnotherHelloWorldServiceGrpc.AnotherHelloWorldServiceBlockingStub anotherBlocking;

    @GET
    @Path("/grpc")
    @Produces(MediaType.APPLICATION_JSON)
    public String helloBlocking() {
        List<String> strings = Arrays.asList("1", "2", "3");
        HelloWorldRequest request = HelloWorldRequest.newBuilder().addAllValues(strings).build();
        return blocking.hello(request).getReturnedValue();
    }


    @GET
    @Path("/another")
    @Produces(MediaType.APPLICATION_JSON)
    public Response anotherBlocking() {
        try {
            AnotherResponse response = anotherBlocking.anotherMessage(AnotherRequest.newBuilder().setValues("ciao").build());
            logger.info("Response {}", response);
            return Response.ok(response.getMessage()).build();
        } catch (io.grpc.StatusRuntimeException ex) {
            logger.error("StatusRuntimeException ", ex);
            return Response.status(Response.Status.BAD_REQUEST)
                    .type(MediaType.APPLICATION_JSON)
                    .entity(ex.getMessage())
                    .build();
        }
    }

}