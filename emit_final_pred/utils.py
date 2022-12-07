import tensorflow as tf

model = tf.keras.models.load_model('saved_model/my_model')

def classif_silo(list_input_image_path, model=model):
    '''
    Detects the probability that the pictures have a silo in them or not.
    Args
        list_input_image_path = list(str) : list of the path of the pictures (png)
        model : trained tensorflow model
    Returns
        prediction = np.array(proba) : array of the probabilities that each picture contains a silo.
    '''
    BATCH_SIZE = 32 # Big enough to measure an F1-score
    AUTOTUNE = tf.data.experimental.AUTOTUNE # Adapt preprocessing and prefetching dynamically
    SHUFFLE_BUFFER_SIZE = 1024 # Shuffle the training data by a chunck of 1024 observations
    CHANNELS = 3
    IMG_SIZE = 256
    
    def parse(input_image_path):
        # Read an image from a file
        image_string = tf.io.read_file(input_image_path)
        # Decode it into a dense vector
        image_decoded = tf.image.decode_jpeg(image_string, channels=CHANNELS)
        # Resize it to fixed shape
        image_resized = tf.image.resize(image_decoded, [IMG_SIZE, IMG_SIZE])
        # Normalize it from [0, 255] to [0.0, 1.0]
        image_normalized = image_resized / 255.0

        return (image_normalized)
    
    dataset = tf.data.Dataset.from_tensor_slices((list_input_image_path))
    dataset = dataset.map(parse, num_parallel_calls=AUTOTUNE)
    
    # This is a small dataset, only load it once, and keep it in memory.
    dataset = dataset.cache()

    # Batch the data for multiple steps
    dataset = dataset.batch(BATCH_SIZE)
    # Fetch batches in the background while the model is training.
    dataset = dataset.prefetch(buffer_size=AUTOTUNE)
    
    prediction = model.predict(dataset)
    
    return prediction

# Example of usage:
#input_image_path1 = 'images_classified/not_silos/silos_256-0-0--6-14-1247-31272.png'
#input_image_path2 = 'images_classified/not_silos/silos_256-0-0--6-14-1281-31369.png'
#pred = classif_silo([input_image_path1, input_image_path2], model)