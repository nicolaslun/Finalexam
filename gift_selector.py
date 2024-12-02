import sys

gifts = [
    "Book", "Toy", "Gadget", "Video Game", "Headphones", 
    "Smartphone", "Laptop", "Watch", "Shoes", "Wallet", 
    "Headset", "Camera", "Drone", "Smart Watch", "Bluetooth Speaker"
]

print("Available Gifts:")
for idx, gift in enumerate(gifts):
    print(f"{idx}: {gift}")

user_input = sys.argv[1] if len(sys.argv) > 1 else ""
selected_indices = [int(idx) for idx in user_input.split(",") if idx.isdigit()]
gift_code = 0
selected_gifts = []

for idx in selected_indices:
    gift_code |= 1 << idx
    selected_gifts.append(gifts[idx])

print(f"\nSelected Gifts: {', '.join(selected_gifts)}")
print(f"Unique Gift Code: {gift_code}")
