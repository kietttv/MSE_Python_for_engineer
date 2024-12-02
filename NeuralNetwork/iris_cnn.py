import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.metrics import Precision

# Tải bộ dữ liệu Iris
iris = load_iris()
X = iris.data  # Dữ liệu đặc trưng
y = iris.target  # Nhãn

# Chuẩn hóa dữ liệu đầu vào
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Chuyển nhãn thành dạng one-hot encoding
encoder = LabelEncoder()
y = encoder.fit_transform(y)
y = np.expand_dims(y, axis=-1)  # Chuyển đổi thành ma trận cột

# Chia bộ dữ liệu thành tập huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình mạng nơ-ron đơn giản
model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))  # Lớp đầu tiên với 8 nút, hàm kích hoạt ReLU
model.add(Dense(3, activation='softmax'))  # Lớp output với 3 nút (3 loại Iris)

# Biên dịch mô hình
model.compile(loss='sparse_categorical_crossentropy',  # Dùng hàm mất mát cho phân loại đa lớp
              optimizer='adam',  # Sử dụng Adam optimizer
              metrics=[Precision()])  # Đánh giá độ chính xác

# Huấn luyện mô hình
model.fit(X_train, y_train, epochs=50, batch_size=8, validation_data=(X_test, y_test))

# Đánh giá mô hình
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Loss: {loss:.4f}, Accuracy: {accuracy*100:.2f}%")
