cfiles = {"train_features":'./examples/data/class_train.features',
                          "train_labels":'./examples/data/class_train.labels',
                          "test_features":'./examples/data/class_test.features',
                          "test_labels":'./examples/data/class_test.labels'}

defparams = {"X":"train_features", "Y":"train_labels"}

experiments = {"mmc_defparams":{
                "learner":"MMC",
                "lpath":"rlscore.learner.mmc",
                "measure":"auc",
                "lfparams": defparams,
                "lparams": {"regparam":1},
                "files": cfiles},
               }