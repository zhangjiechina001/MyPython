import tensorflow as tf
import tensorflow as tf1

def input_fn():
    return {'age':[19,23,34,30,60,55,36],'name':['Robert','David','Kelly','Rose','Hayes','Luis','Lili']},[0,0,1,1,0,0,1]

def input_fn_predict():
    dataset=tf.data.Dataset.from_tensor_slices(({'age':[23,33,58,20,59]},[0,1,0,0,0]))
    dataset=dataset.batch(10)
    return dataset

def main():
    age=tf.feature_column.numeric_column('age')

    estimater=tf.estimator.DNNClassifier(feature_columns=[age],hidden_units=[1000])

    estimater.train(input_fn=input_fn(),steps=10000)
    evaluation=estimater.evaluate(input_fn=input_fn_predict())
    print('\nAccuracy:{accuracy:0.3f}\n'.format(**evaluation))

    prediction=estimater.predict(input_fn=input_fn_predict())
    for idx,predict in enumerate(prediction):
        class_id=predict['class_ids'][0]
        problity=predict['probabilities'][class_id]
        print('{}:label:{},prob:{}'.format(idx,class_id,problity))

if __name__=="__main__":
    tf.logging.set_verbosity(tf.logging.INFO)
tf.app.run(main())