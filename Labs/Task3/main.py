import sys
sys.path.append('../Utils')
import ioutils
from quadro import quadro
import my_parser
from point import point

file = my_parser.create_parser().parse_args().name
data = ioutils.read_array2d(file)
points = []
for i in range(len(data)):
    points.append([point(data[i][0], data[i][1]), point(data[i][2], data[i][3])])
quadros = []
for i in range(len(points)):
    quadros.append(quadro(points[i][0], points[i][1]))

result = []
for i in range(len(quadros)):
    q = quadros[i]
    flag = False
    for j in range(len(quadros)):
        if(i != j):
            p1 = quadros[j].v1
            p2 = quadros[j].v2
            p3 = point(quadros[j].v1.x, quadros[j].v2.y)
            p4 = point(quadros[j].v2.x, quadros[j].v1.y)

            flag = q.is_point_inside(p1) or q.is_point_inside(p2) or q.is_point_inside(p3) or q.is_point_inside(p4)
    if not flag:
        result.append(q)

print([(q.v1.x, q.v1.y, q.v2.x, q.v2.y) for q in result])
