class montecarlo:
    def __init__(self, func, setup=None, teardown=None, output=None):
        self.func = func
        self.setup = setup
        self.teardown = teardown
        if output:
            self.output = output
        else:
            self.output = self.print_results

    @staticmethod
    def probability(success, iterations):
        return float(success)/iterations

    @staticmethod
    def print_results(success, iterations, final=False):
        if final:
            print('======================')
            print('======= FINAL ========')
            print('======================')
        print('Iteration #' + str(iterations) + ': ' + str(montecarlo.probability(success, iterations)))

    def run(self, iterations=1000000, output_every=10000):
        g = {}
        if self.setup is not None:
            g = self.setup()

        success = 0
        for i in range(1, iterations+1):
            if self.func(g):
                success += 1
            if (i % output_every == 0):
                self.output(success, iterations=i)
        self.output(success, iterations, final=True)

        if self.teardown is not None:
            self.teardown()

        return self.output(success, iterations)
