import torch

print("PyTorch Exercise 1: Gradient Descent")
print("-------------------------------------")
print()
print("Model:        ŷ = w × x")
print("Loss:         L = (ŷ − y)²")
print()

x = float(input("Enter input x: "))
y = float(input("Enter target y: "))
w_value = float(input("Enter starting w: "))

w = torch.tensor(w_value, requires_grad=True)

learning_rate = 0.01
iterations = 10

print()
print("Learning process")
print("----------------")

for i in range(iterations):
    # Forward pass
    prediction = w * x

    # Calculate loss
    loss = (prediction - y) ** 2

    # Remove previous gradient
    w.grad = None

    # Calculate gradient
    loss.backward()

    gradient = w.grad.item()

    print()
    print("Iteration:", i)
    print("  w:", w.item())
    print("  prediction:", prediction.item())
    print("  loss:", loss.item())
    print("  gradient:", gradient)

    # Update w
    with torch.no_grad():
        w -= learning_rate * w.grad

print()
print("Final result")
print("------------")
print("w:", w.item())
print("prediction:", (w * x).item())
print("loss:", loss.item())