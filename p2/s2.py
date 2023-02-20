import tensorflow as tf

model = tf.keras.Sequencial()

model.add(tf.keras.layers.Convo2D(32,3))
model.add(tf.keras.layers.MaxPool2D())
model.add(tf.keras.layers.Relu())
model.add(tf.keras.layers.Convo2D(64,4))
model.add(tf.keras.layers.MaxPool2D())
model.add(tf.keras.layers.Relu())
model.add(tf.keras.layers.Reshape(target_shape=(25*64)))
model.add(tf.keras.layers.Dense(100))
model.add(tf.keras.layers.Relu())
model.add(tf.keras.layers.Dense(100))
model.add(tf.keras.layers.Relu())
model.add(tf.keras.layers.Dense(10))
model.add(tf.keras.layers.Softmax())

model.compile(optimizer=tf.keras.optimizer.Adam(0.01),
              loss = tf.keras.losses.CategoricalCrossEntropy(),
              metrics =[tf.keras.metrics.CategoricalAccurcy()]
              )
