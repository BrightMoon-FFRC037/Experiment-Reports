
# %%
# Step 1: Read the picture file
import pandas as pd
from PIL import Image
img = Image.open('Spectrum.jpg')
img.show()

# %%
# Step 2: Convert the picture to an array of pixel values
img_array = img.convert('RGB')
print(type(img_array))
array = pd.DataFrame(img_array)


#%%
# Step 3: Flatten the array
img_array_flat = img_array.resize((img.width * img.height, 3))


# Step 4: Create a dataframe
df = pd.DataFrame(img_array_flat, columns=['R', 'G', 'B'])

# Display the dataframe
print(df)
