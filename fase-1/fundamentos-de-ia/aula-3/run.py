import torch
import torch.nn as nn           # responsável por estruturar a rede
import torch.optim as optim     # responsável por ajustar e melhorar o modelo

# dados utilizados para o modelo utiliza para aprender
X = torch.tensor([[5.0],[10.0],[10.0],[5.0],[10.0],
                  [5.0],[10.0],[10.0],[5.0],[10.0],
                  [5.0],[10.0],[10.0],[5.0],[10.0],
                  [5.0],[10.0],[10.0],[5.0],[10.0]], dtype=torch.float32)

# resultados esperados de acordo com os dados do X
y = torch.tensor([[30.5],[63.0],[67.0],[29.0],[62.0],
                  [30.5],[63.0],[67.0],[29.0],[62.0],
                  [30.5],[63.0],[67.0],[29.0],[62.0],
                  [30.5],[63.0],[67.0],[29.0],[62.0]], dtype=torch.float32)

# rede neural - cria camadas para aprendizado 
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Atualizando para aceitar apenas 1 valor de entrada, pois agora temos apenas a distância
        self.fc1 = nn.Linear(1, 5) # De 2 para 1 na entrada
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x
    
model = Net()

criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# treino da rede
# loop é onde é feito as previsões e também o calculo das previsões erradas, chamadas de perda
# com a perde a rede vai se ajustando os pesos para melhorar as previsões
for epoch in range(1000):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

    if epoch % 100 == 99:
        print(f'Epoch {epoch+1}, Loss: {loss.item()}')

# teste - checar quanto tempo um corredor demoraria para percorrer 10km
with torch.no_grad():
    predicted = model(torch.tensor([[10.0]], dtype=torch.float32))
    print(f'Previsão de tempo de conclusão: {predicted.item()} minutos')

'''
A função que calculas as perdas irá gerar o seguinte resultado:
Epoch 100, Loss: 341.13812255859375
Epoch 200, Loss: 285.5550842285156
Epoch 300, Loss: 284.5774841308594
Epoch 400, Loss: 284.560302734375
Epoch 500, Loss: 284.55999755859375
Epoch 600, Loss: 284.55999755859375
Epoch 700, Loss: 284.55999755859375
Epoch 800, Loss: 284.55999755859375
Epoch 900, Loss: 284.55999755859375
Epoch 1000, Loss: 284.55999755859375

Quanto menor a perda melhor o modelo está aprendendo
Quando o valor da perda fica estagnado pode significar alguns coisas:
    - o modelo parou de aprender, pois os dados de entrada já não são mais significantes. 
        Nesse caso o modelo chegou no ponto de convergência
    - o modelo também pode estar se sobre ajustar nos dados de treinamento, 
        isso significa que o modelo deve estar captando algum ruído ou trazendo dados irrelavantes 
        dos dados de treinamento. Para resolver isso poderia mudar a estrutura, por exemplo, 
        adicionar mais camadas de neuronios para aprender padrões mais complexos

'''