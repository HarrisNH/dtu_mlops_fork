import torch
import torchvision.models as models
from torch.profiler import profile, ProfilerActivity,tensorboard_trace_handler

model = models.resnet18().to("cpu")
inputs = torch.randn(5, 3, 224, 224)

# Start profiling with `on_trace_ready` to collect traces
with profile(
    activities=[ProfilerActivity.CPU],
    record_shapes=True,
    profile_memory=True,
    with_stack=True,
    on_trace_ready=tensorboard_trace_handler("./log/resnet18")
) as prof:

    for i in range(10):
            model(inputs)
            prof.step()

# Check profiling results
print("Number of profiled events:", len(prof.key_averages()))
print(prof.key_averages().table(sort_by="self_cpu_memory_usage", row_limit=10))

prof.export_chrome_trace("trace.json")