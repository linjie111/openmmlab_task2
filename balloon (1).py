_base_ = ['mask_rcnn_x101_32x4d_fpn_2x_coco.py']

data = dict(
    
      train=dict(
        ann_file='/openbayes/home/train_data.json',
        img_prefix='/openbayes/input/input0/balloon/train',
        classes = ("balloon",)
      ),
      val=dict(
        ann_file='/openbayes/home/val_data.json',
        img_prefix='/openbayes/input/input0/balloon/val',
        classes = ("balloon",)
      ),
      test=dict(
        ann_file='/openbayes/home/val_data.json',
        img_prefix='/openbayes/input/input0/balloon/val',
        classes = ("balloon",)
      )   
)

model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=1
        ),
        mask_head=dict(
            num_classes=1
        )
    )
)