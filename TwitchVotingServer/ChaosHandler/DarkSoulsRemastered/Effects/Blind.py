import asyncio

from ChaosHandler.DarkSoulsRemastered.Memory import BaseAddress, PointerAddress
from ChaosHandler.Effect import BaseEffect
from pymem import memory


class Blind(BaseEffect):
    name = "Blinded"

    @classmethod
    async def start(cls, pm, module):
        BaseCAR = BaseAddress.BaseCAR(pm, module)
        DrawDistancePointer = PointerAddress.DrawDistance(pm, BaseCAR)

        memory.write_float(pm.process_handle, DrawDistancePointer, 1)
        await asyncio.sleep(cls.seconds)
        memory.write_float(pm.process_handle, DrawDistancePointer, 3100)
