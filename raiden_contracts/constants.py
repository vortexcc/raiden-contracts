from enum import IntEnum

# Contract names
CONTRACT_ENDPOINT_REGISTRY = 'EndpointRegistry'
CONTRACT_HUMAN_STANDARD_TOKEN = 'HumanStandardToken'
CONTRACT_TOKEN_NETWORK_REGISTRY = 'TokenNetworkRegistry'
CONTRACT_TOKEN_NETWORK = 'TokenNetwork'
CONTRACT_SECRET_REGISTRY = 'SecretRegistry'
CONTRACT_CUSTOM_TOKEN = 'CustomToken'
CONTRACT_CUSTOM_TOKEN_NO_DECIMALS = 'CustomTokenNoDecimals'
CONTRACT_MONITORING_SERVICE = 'MonitoringService'
CONTRACT_RAIDEN_SERVICE_BUNDLE = 'RaidenServiceBundle'

# TokenNetworkRegistry
EVENT_TOKEN_NETWORK_CREATED = 'TokenNetworkCreated'

# TokenNetwork
EVENT_CHANNEL_OPENED = 'ChannelOpened'
EVENT_CHANNEL_DEPOSIT = 'ChannelNewDeposit'
EVENT_CHANNEL_WITHDRAW = 'ChannelWithdraw'
EVENT_CHANNEL_BALANCE_PROOF_UPDATED = 'NonClosingBalanceProofUpdated'
EVENT_CHANNEL_CLOSED = 'ChannelClosed'
EVENT_CHANNEL_SETTLED = 'ChannelSettled'
EVENT_CHANNEL_UNLOCKED = 'ChannelUnlocked'

# SecretRegistry
EVENT_SECRET_REVEALED = 'SecretRevealed'

# EndpointRegistry
EVENT_ADDRESS_REGISTERED = 'AddressRegistered'

# Timeouts
TEST_SETTLE_TIMEOUT_MIN = 5
TEST_SETTLE_TIMEOUT_MAX = 100000

DEPLOY_SETTLE_TIMEOUT_MIN = 500  # ~ 2 hours
DEPLOY_SETTLE_TIMEOUT_MAX = 555428  # ~ 3 months

# Channel states
CHANNEL_STATE_NONEXISTENT = 0
CHANNEL_STATE_OPENED = 1
CHANNEL_STATE_CLOSED = 2
CHANNEL_STATE_SETTLED = 3
CHANNEL_STATE_REMOVED = 4

# Temporary token deposit limits for the Red Eyes release
MAX_TOKENS_DEPLOY = 100


class ChannelInfoIndex(IntEnum):
    SETTLE_BLOCK = 0
    STATE = 1


class ParticipantInfoIndex(IntEnum):
    DEPOSIT = 0
    WITHDRAWN = 1
    IS_CLOSER = 2
    BALANCE_HASH = 3
    NONCE = 4
    LOCKSROOT = 5
    LOCKED_AMOUNT = 6
