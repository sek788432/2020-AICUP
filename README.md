# 2020_AICUP
Name Entity Recognition in Medical Data Contest

## Requirements

```sh
pip install "kashgari>=1.1,<2.0"
pip install "tensorflow>=1.14,<2.0"
```

### Pre-trained BERT model:
- [Google BERT](./https://github.com/google-research/bert)
- [Chinese-BERT-wwm](./https://github.com/ymcui/Chinese-BERT-wwm)

### BERT Transfer Learning Framework
- [Kashgari](./https://github.com/BrikerMan/Kashgari)

---

## Data
> Data files won't be uploaded due to privacy concerns.

### Sample Training Data
![image](./readme_img/1.PNG)
### Sample Test Data
![image](./readme_img/2.PNG)
### Output Format
![image](./readme_img/6.PNG)

---

## [Name Entity Recognition Introduction](./NER_intro.ppt)
![image](./readme_img/3.PNG)

---

## Method
### Transfer Learning with pre-trained BERT and add BiLSTM + CRF layer
![image](./readme_img/4.png)

### Bagging the outputs of all kinds of pre-trained BERT
![image](./readme_img/5.PNG)

---

## Result on Public Leader Board
### Google BERT Batch Size 24
![image](./readme_img/7.PNG)
### Google BERT Batch Size 36
![image](./readme_img/8.PNG)
### Roberta wwm
![image](./readme_img/9.PNG)
### BERT wwm
![image](./readme_img/10.PNG)
### Bagging the outputs
![image](./readme_img/11.PNG)

---

## Reference
https://www.semanticscholar.org/paper/A-BERT-BiLSTM-CRF-Model-for-Chinese-Electronic-Zhang-Jiang/bd01b18df9a39cdd5c66f44051d62f176e9c8e7e
