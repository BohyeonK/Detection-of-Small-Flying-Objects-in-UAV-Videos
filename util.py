def get_parser():
    """Get parser object."""

    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input",
                        dest="input",
                        help="Path to input",
                        default="/home/research/vladan/data/AID",
                        required=False)
    parser.add_argument("-o", "--output",
                        dest="output",
                        help="Path to output",
                        default="weights.h5",
                        required=False)
    parser.add_argument("-m", "--map",
                        dest="heat",
                        help="Path to output",
                        default="mapa.npy",
                        required=False)
    parser.add_argument("-b", "--bgsub",
                        dest="bgsub",
                        help="Path to directory with bgsub files",
                        default="weights.h5",
                        required=False)
    parser.add_argument("-g", "--gray",
                        dest="gray",
                        help="Path to directory with gray files",
                        default="weights.h5",
                        required=False)
    parser.add_argument("-v", "--video",
                        dest="video",
                        help="Path to directory with gray files",
                        default="weights.h5",
                        required=False)
    parser.add_argument("-a", "--mask",
                        dest="mask",
                        help="Path to directory with mask files",
                        default="weights.h5",
                        required=False)
    parser.add_argument("-c", "--combined",
                        dest="combined",
                        help="Use combinded",
                        action='store_true',
                        required=False)
    parser.add_argument("-d", "--depth",
                        dest="depth",
                        help="Depth",
                        type=int,
                        default=3,
                        required=False)
    parser.add_argument("-t", "--type",
                        dest="type",
                        help="Type of dataset",
                        default="weights.h5",
                        required=False)
    parser.add_argument("--num_out_channels",
                        dest="num_out_channels",
                        help="Number of output channels",
                        type=int,
                        default=1,
                        required=False)
    parser.add_argument("--train_data",
                        dest="train_data",
                        help="Train data",
                        required=False)
    parser.add_argument("--val_data",
                        dest="val_data",
                        help="Validation data",
                        required=False)
    parser.add_argument("--test_data",
                        dest="test_data",
                        help="Test data",
                        required=False)
    parser.add_argument("--model",
                        dest="model",
                        help="Model path",
                        required=False)
    parser.add_argument("--thr",
                        dest="thr",
                        help="Threshold",
                        type=float,
                        default=0.04,
                        required=False)
    return parser
