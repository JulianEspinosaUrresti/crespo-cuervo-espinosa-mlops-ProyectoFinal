import onnx
from onnx import helper, TensorProto

input_tensor = helper.make_tensor_value_info("input", TensorProto.FLOAT, [1, 3])
output_tensor = helper.make_tensor_value_info("output", TensorProto.FLOAT, [1, 1])

node = helper.make_node(
    "ReduceSum",
    inputs=["input"],
    outputs=["output"],
    axes=[1],
    keepdims=1
)

graph = helper.make_graph(
    [node],
    "credit_scoring_model",
    [input_tensor],
    [output_tensor]
)

model = helper.make_model(graph, producer_name="proyecto_final_mlops")
onnx.save(model, "models/credit_model.onnx")

print("Modelo ONNX creado en models/credit_model.onnx")