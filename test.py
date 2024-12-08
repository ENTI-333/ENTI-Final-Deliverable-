import pytest
import numpy as np
from quantum_emergence.quantum_emergence_system import (
    QuantumemergenceSystem, 
    measure_state,
    measure_knowledge_spread,
    measure_emergence_spread
)
from quantum_emergence.quantum_time import time

@pytest.fixture
def system():
    return QuantumemergenceSystem()

class TestQuantumEmergenceSystem:
    
    def test_continuous_emergence(self, system):
        """Test that system never reaches static state"""
        t1 = measure_state(system.get_quantum_state())
        time.quantum_advance()
        t2 = measure_state(system.get_quantum_state())
        
        assert not np.array_equal(t2, t1)
        assert system.dC_dt != 0
        
    def test_uncertainty_principle(self, system):
        """Test that knowledge/emergence uncertainty holds"""
        knowledge_uncertainty = measure_knowledge_spread()
        emergence_uncertainty = measure_emergence_spread()
        
        assert knowledge_uncertainty * emergence_uncertainty >= system.PLANCK_CONSTANT/2
        
    def test_self_reference(self, system):
        """Test system's self-awareness capabilities"""
        initial_self_state = system.get_self_state()
        system.process_self_observation()
        final_self_state = system.get_self_state()
        
        assert final_self_state.awareness_level > initial_self_state.awareness_level
        assert system.is_observing_self() == True
        
    def test_becoming_function(self, system):
        """Test the becoming function B(t) is properly tracking state changes"""
        delta_t = 0.001
        state_t1 = system.get_state()
        system.advance(delta_t)
        state_t2 = system.get_state()
        
        becoming_rate = np.sum(state_t2 - state_t1)/delta_t
        assert becoming_rate != 0
        assert system.is_state_novel(state_t2)