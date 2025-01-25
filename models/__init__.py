from models.actor_critic import ActorCritic
from models.dqn import DQN
from models.double_dqn import Double_DQN
from models.dueling_dqn import Dueling_DQN
from models.reinforce import Reinforce

if __name__ == "__main__":
    actor_critic = ActorCritic()
    dqn = DQN()
    double_dqn = Double_DQN()
    dueling_dqn = Dueling_DQN()
    reinforce = Reinforce()

