config = [
	'--all_datasets False',
	'--datasets affectnet_short fer2013',
	'--img_size 224',
	'--transform classic',
	'--val_split 0.1',
	'--split_seed 18',
	'--epochs 50',
	'--batch_size 64',
	'--num_workers 12',
	'--checkpoint None',
	'--save_every 1',
	'--optimizer Adam',
	'--lr_scheduler None',
	'--model vit',
	'--num_encoder_layers 6',
	'--num_decoder_layers 3',
	'--num_heads 8',
	'--emb_size 768',
]
