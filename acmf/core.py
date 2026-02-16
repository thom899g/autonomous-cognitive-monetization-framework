"""
The core module of ACMF defines the primary classes and interfaces that enable cognitive upgrades, resource allocation, and error recovery. It serves as the foundation for building intelligent automation systems.
"""

from typing import Dict, Any
from logging import Logger
from .components.resource_allocator import ResourceAllocator
from .components.cognitive_upgrade_engine import CognitiveUpgradeEngine
from .components.error_recovery_module import ErrorRecoveryModule

class FrameworkCore:
    """
    The central class managing the ACMF system. It integrates various components to achieve mission objectives.
    
    Attributes:
        resource_allocator: Manages task distribution across resources.
        cognitive_upgrader: Enhances AI capabilities through feedback loops.
        error_recoverer: Handles exceptions and ensures system resilience.
        logger: Logs system activities for monitoring and debugging.
    """
    
    def __init__(self, config: Dict[str, Any], logger: Logger):
        self.resource_allocator = ResourceAllocator(config, logger)
        self.cognitive_upgrader = CognitiveUpgradeEngine(config, logger)
        self.error_recoverer = ErrorRecoveryModule(config, logger)
        self.logger = logger
        
    def allocate_resources(self, task: str) -> bool:
        """
        Allocates resources to a given task.
        
        Args:
            task: The task to be executed.
            
        Returns:
            True if allocation is successful, False otherwise.
        """
        try:
            self.resource_allocator.allocate(task)
            return True
        except Exception as e:
            self.error_recoverer.handle_error(e, "Resource allocation failed")
            return False
        
    def perform_upgrade(self, model: Any) -> Any:
        """
        Upgrades an AI model based on feedback.
        
        Args:
            model: The AI model to be upgraded.
            
        Returns:
            The upgraded model or the original model if upgrade fails.
        """
        try:
            return self.cognitive_upgrader.upgrade(model)
        except Exception as e:
            self.error_recoverer.handle_error(e, "Cognitive upgrade failed")
            return model