from concurrent import futures

import grpc

import course_service_pb2
import course_service_pb2_grpc

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        return course_service_pb2.GetCourseResponse(request.course_id, request.course_name, request.description)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    server.add_insecure_port('[::]:50051')

    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
