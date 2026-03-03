phone = "9030108465"
# Keep first 2 and last 2, mask the middle
masked = phone[:2] + ("*" * 6) + phone[-2:]

print(f"Original: {phone}")
print(f"Masked: {masked}")
