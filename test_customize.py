
import random
from algorithm.core import run_gavrptw
from algorithm.core import run_gavrptw_with_stations

def test_run_gavrptw_executes():
    """
    测试 run_gavrptw 是否可以成功运行并不抛出异常
    """
    random.seed(64)
    instance_name = 'c105'

    run_gavrptw_with_stations(
        instance_name=instance_name,
        unit_cost=8.0,
        init_cost=100.0,
        wait_cost=0,
        delay_cost=0,
        ind_size=18,
        pop_size=1000,
        cx_pb=0.85,
        mut_pb=0.02,
        n_gen=100,  # 缩短测试时间
        energy_per_km=1,
        export_csv=False,
        customize_data=True

    )
