from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.yaml")  # build a new model from scratch
    model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    model.train(data="config.yaml", epochs=40)  # train the model
    metrics = model.val() 
    results = model("train")  # predict on an image

if _name_ == '_main_':
    import multiprocessing
    multiprocessing.freeze_support()
    main()