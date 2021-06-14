NAME      := simul
SRC_EXT   := gz
TEST_PACKAGES := $(NAME) $(NAME)-mpich $(NAME)-openmpi3

include packaging/Makefile_packaging.mk

test:
	$(call install_repos,$(NAME)@$(BRANCH_NAME):$(BUILD_NUMBER))
	yum -y install $(NAME)
