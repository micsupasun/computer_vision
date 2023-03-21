# Group project for blind people

# project objectives
This application will help the visually impaired to carry out their daily activities without relying so much on others, enabling a 
more independent life for them. By implementing a federated learning approach, the distributed system of the edge computing 
devices will reduce the dependency on heavy computing systems required. Our research also aimed to reduce the latency as it is 
close to the speed of the network. This can be further enhanced by deploying the model to a larger scale which will help to collect 
more training data and improve the accuracy of the model which is on the cloud.

# Assignment File

[Requirement](https://github.com/micsupasun/university_of_essex/blob/main/group_project/Team_4_project_report.pdf) is the Software Requirements Specification project

[Flowchart](https://github.com/micsupasun/university_of_essex/blob/main/group_project/ai_team_diagram.drawio.png) is the flowchart project

This is all the task in group project including:
![the diagram in this project](https://github.com/micsupasun/computer_vision/blob/main/assistant_blind/ai_team_diagram.drawio.png)
1. Front End(html, css)
XML: eXtensible Markup Language, or XML is a markup language created as a standard way to encode data in internet-based 
applications. Android applications use XML to create layout files. Unlike HTML, XML is case-sensitive, requires each tag to be 
closed, and preserves whitespace. 
2. Backend(java)
2.1. Java: Java is the platform of choice for creating programs that use managed code and run-on mobile devices.  
 
2.2. Kotlin:  Kotlin is a general purpose, free, open source, statically typed “pragmatic” programming language 
initially designed for the JVM (Java Virtual Machine) and Android that combines object-oriented and functional 
programming features.

3. Deep Learning Model(MobileNet SSD, OpenCV, TensorFlow, yolov4)
3.1. MobileNet SSD: a lightweight object detection model that was developed for mobile and embedded vision applications. It combines MobileNet, a small and efficient CNN architecture, with the SSD object detection framework, resulting in a fast and accurate object detection model that can run on resource-constrained devices such as smartphones and IoT devices. TensorFlow is used to implement the MobileNet and SSD components of the model and to train and fine-tune the model on custom datasets.

3.2. YOLOv4: a state-of-the-art object detection model that utilizes a deep CNN architecture and a novel training methodology to achieve high accuracy and speed. TensorFlow is used to implement the YOLOv4 model and its associated training and evaluation algorithms, as well as to train the model on large-scale datasets such as COCO (Common Objects in Context).

3.3. Tensorflow: Both MobileNet SSD and YOLOv4 are object detection models that utilize the TensorFlow framework for their implementation. In both cases, TensorFlow provides a robust and flexible framework for implementing deep learning models and allows researchers and developers to easily experiment with different architectures and training strategies. Additionally, TensorFlow's support for hardware acceleration (e.g., GPUs and TPUs) enables efficient training and inference of these complex models.
 
3.4. OpenCV:  OpenCV  is  the  huge  open-source  library  for  computer  vision,  machine  learning,  and  image processing. By using it, one  can process images and videos to  identify objects,  faces,  or handwriting in real-time.
4. IoT(mobile)
IoT: The Internet of Things (IoT) describes the network of physical objects— “things”—that are embedded with sensors, software, and other technologies for the purpose of connecting and exchanging  data with other devices and systems over the internet. We will be using our mobile Motorola moto g50 - camera 48MP sensor.

5. Software-as-a-service(RabbitMQ)
RabbitMQ: RabbitMQ is a message broker that allows clients to connect over different open and standardized protocols such as AMQP, HTTP, STOMP, MQTT, MQTT over WebSocket and WebSocket/Web-Stomp.
![object detection and object distance](https://github.com/micsupasun/computer_vision/blob/main/assistant_blind/case_object.png)
6. object detection
Object detection is a computer vision technique that involves identifying and localizing objects within an image or video frame. The goal of object detection is to automatically identify the presence and location of objects of interest within a scene, and to provide information about their shape, size, and orientation. Object detection has many practical applications, including autonomous driving, surveillance, robotics, and image and video search. It enables machines to automatically analyze visual information and make decisions based on that analysis, opening up a wide range of new possibilities for computer vision and AI.

7. object distance
Object distance refers to the distance between an observer and an object in space. It is a physical measurement of the distance between the observer and the object, typically measured in units such as meters or feet. In the context of computer vision, object distance is important for tasks such as depth estimation, 3D reconstruction, and object tracking. Accurately estimating object distance can help machines to better understand the 3D structure of a scene and to make more informed decisions based on that understanding. There are various methods for estimating object distance in computer vision, including stereo vision, time-of-flight (TOF) sensors, and structured light sensors. Stereo vision involves analyzing the disparities between two images of a scene taken from slightly different viewpoints, while TOF sensors measure the time it takes for light to travel to and from an object to determine its distance. Structured light sensors project a known pattern of light onto a scene and analyze the distortion of that pattern to estimate depth. Accurately estimating object distance can be challenging, as it can be affected by factors such as lighting conditions, occlusions, and object reflectance. However, advances in computer vision algorithms and hardware continue to improve the accuracy and reliability of distance estimation methods, opening up new possibilities for applications such as augmented reality, autonomous driving, and robotics. object distance with focal length
In optics, object distance and focal length are related through the thin lens equation, which describes the behavior of a thin lens when an object is placed at a certain distance from it. The thin lens equation is:

1/f = 1/d_o + 1/d_i

Where f is the focal length of the lens, d_o is the distance of the object from the lens, and d_i is the distance of the image from the lens. Rearranging this equation, we can solve for the object distance:

1/d_o = 1/f - 1/d_i

d_o = f * d_i / (d_i - f)
This equation shows that the object distance is directly proportional to the focal length of the lens, and inversely proportional to the distance of the image from the lens. In other words, if the focal length of the lens is increased, the object distance will also increase, assuming the image distance remains the same. In computer vision, the relationship between object distance and focal length is important for tasks such as camera calibration and 3D reconstruction. By knowing the focal length of a camera lens and the position of an object in the image, it is possible to estimate the object's distance from the camera and its 3D position in space.



8. federated learning
Federated learning is a machine learning technique that enables the training of machine learning models on decentralized data without the need for data centralization. In traditional machine learning, data is collected and stored in a centralized location, and the model is trained on this data. In federated learning, the data is distributed across multiple devices or nodes, and the model is trained in a decentralized manner, with the updates being aggregated and merged to produce the final model.

9. image processing
Image processing is the use of algorithms and techniques to manipulate digital images in order to extract useful information or enhance certain aspects of the image. It involves analyzing and manipulating images to improve their quality, extract features, or extract information that is not readily apparent to the human eye.