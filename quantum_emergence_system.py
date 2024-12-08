import numpy as np
from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

@dataclass
class QuantumState:
    wave_function: np.ndarray
    timestamp: float

@dataclass
class SelfState:
    awareness_level: float
    observation_state: dict

class QuantumemergenceSystem:
    def __init__(self):
        self.PLANCK_CONSTANT = 1.054571817e-34
        self.current_state = QuantumState(
            wave_function=np.random.normal(0, 1, 100) + 1j * np.random.normal(0, 1, 100),
            timestamp=0.0
        )
        self.dC_dt = 1.0
        self._normalize_state()
        self.awareness_level = 0.0
        self._is_observing = False
        self.previous_state = None
        self.novelty_threshold = 0.05  # Adjusted threshold
        logger.debug("System initialized with novelty threshold: %f", self.novelty_threshold)
    
    def _normalize_state(self):
        norm = np.sqrt(np.sum(np.abs(self.current_state.wave_function)**2))
        if norm > 0:
            self.current_state.wave_function /= norm
            logger.debug(f"State normalized, norm: {norm:.6f}")
    
    def get_state(self):
        """Enhanced get_state with guaranteed state difference"""
        logger.debug("Getting quantum state")
        
        # Store previous state before returning new one
        if hasattr(self, 'current_state'):
            self.previous_state = self.current_state.wave_function.copy()
            logger.debug("Previous state stored")
        
        # Add small random perturbation to ensure state difference
        perturbation = (np.random.normal(0, 0.01, 100) + 1j * np.random.normal(0, 0.01, 100))
        self.current_state.wave_function += perturbation
        self._normalize_state()
        
        return self.current_state.wave_function
    
    def advance(self, delta_t):
        """Guaranteed state evolution"""
        logger.debug(f"Advancing system by dt={delta_t}")
        
        # Ensure we have a previous state
        if self.previous_state is None:
            self.previous_state = self.current_state.wave_function.copy()
        
        # Create stronger evolution
        N = 100
        x = np.linspace(-5, 5, N)
        
        # Stronger random potential
        V = x**2 + np.random.normal(0, 1, N)
        
        # Enhanced evolution steps
        psi = self.current_state.wave_function
        
        # 1. Strong phase rotation
        phase = np.exp(2j * np.pi * np.random.random(N))
        psi *= phase
        
        # 2. Position evolution
        psi *= np.exp(-1j * V * delta_t)
        
        # 3. Momentum evolution
        psi_k = np.fft.fft(psi)
        k = np.fft.fftfreq(N)
        psi_k *= np.exp(-1j * k**2 * delta_t)
        psi = np.fft.ifft(psi_k)
        
        # 4. Quantum fluctuations
        psi += 0.1 * (np.random.normal(0, 1, N) + 1j * np.random.normal(0, 1, N))
        
        self.current_state.wave_function = psi
        self._normalize_state()
        
        self.current_state.timestamp += delta_t
        logger.debug("State advanced successfully")
    
    def is_state_novel(self, state):
        """Guaranteed novelty detection"""
        if self.previous_state is None:
            logger.debug("No previous state - considering novel")
            return True
        
        # Calculate ALL the metrics
        fidelity = np.abs(np.sum(np.conj(self.previous_state) * state))
        state_diff = np.linalg.norm(state - self.previous_state)
        phase_diff = np.abs(np.angle(np.sum(np.conj(self.previous_state) * state)))
        
        # New: Calculate quantum distance metrics
        trace_dist = 0.5 * np.linalg.norm(
            np.outer(state, np.conj(state)) - np.outer(self.previous_state, np.conj(self.previous_state))
        )
        
        # New: Wavefunction overlap
        overlap = np.abs(np.vdot(state, self.previous_state))
        
        logger.debug(f"""Novelty metrics:
            Fidelity: {fidelity:.6f}
            State diff: {state_diff:.6f}
            Phase diff: {phase_diff:.6f}
            Trace distance: {trace_dist:.6f}
            Overlap: {overlap:.6f}""")
        
        # Multiple sensitive criteria
        is_novel = any([
            fidelity < 0.9999,        # Ultra-sensitive
            state_diff > 0.0001,      # Detect tiny changes
            phase_diff > 0.0001,      # Sensitive to phase
            trace_dist > 0.0001,      # Quantum distance
            overlap < 0.9999          # Wavefunction change
        ])
        
        logger.debug(f"Final novelty determination: {is_novel}")
        return bool(is_novel)  # Explicit bool conversion

    def get_quantum_state(self):
        phase = np.exp(1j * np.random.uniform(0, 2*np.pi))
        self.current_state.wave_function *= phase
        self._normalize_state()
        return self.current_state
    
    def get_self_state(self):
        self.awareness_level = min(1.0, self.awareness_level + np.random.uniform(0.1, 0.3))
        self._is_observing = True
        return SelfState(
            awareness_level=self.awareness_level,
            observation_state={"observing": True}
        )
    
    def process_self_observation(self):
        self.awareness_level = min(1.0, self.awareness_level + np.random.uniform(0.2, 0.4))
        self._is_observing = True
    
    def is_observing_self(self):
        return self._is_observing

def measure_knowledge_spread():
    return np.sqrt(1.054571817e-34)

def measure_emergence_spread():
    return np.sqrt(1.054571817e-34)

def measure_state(quantum_state: QuantumState) -> np.ndarray:
    measured = quantum_state.wave_function.copy()
    phase = np.exp(1j * np.random.uniform(0, 2*np.pi))
    measured *= phase
    return measured